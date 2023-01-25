# import ptm_torrent.huggingface.createSchema as createSchema
import ptm_torrent.huggingface.downloadJSON as downloadJSON
import ptm_torrent.huggingface.downloadRepos as downloadRepos
import ptm_torrent.huggingface.setupFileSystem as setupFS

shrinkage: float = 0.1

if __name__ == "__main__":
    setupFS.main()
    downloadJSON.main()
    downloadRepos.main(shrinkage)
    # createSchema.main()
