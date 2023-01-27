from os import environ

import ptm_torrent.huggingface.createSchema as createSchema
import ptm_torrent.huggingface.downloadJSON as downloadJSON
import ptm_torrent.huggingface.downloadRepos as downloadRepos
import ptm_torrent.huggingface.setupFileSystem as setupFS
import ptm_torrent.huggingface.splitRepos as splitRepos

if __name__ == "__main__":
    shrinkage: float | str | None

    shrinkageEnvironmentVariable: str = "HF_TORRENT_SHRINKAGE"
    shrinkageEnvironmentValue: str = environ.get(shrinkageEnvironmentVariable)

    try:
        shrinkage = float(shrinkageEnvironmentValue)
    except ValueError:
        print(f"Invalid value for {shrinkageEnvironmentVariable}. Defaulting to 0.1")
        shrinkage = 0.1
    except TypeError:
        print(f"Invalid value for {shrinkageEnvironmentVariable}. Defaulting to 0.1")
        shrinkage = 0.1

    if shrinkage > 1 or shrinkage <= 0:
        print(f"Invalid value for {shrinkageEnvironmentVariable}. Defaulting to 0.1")
        shrinkage = 0.1

    setupFS.main()
    downloadJSON.main()
    splitRepos.main(shrinkage)
    createSchema.main()
