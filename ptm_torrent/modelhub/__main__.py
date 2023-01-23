import ptm_torrent.modelhub.createSchema as createSchema
import ptm_torrent.modelhub.downloadJSON as downloadJSON
import ptm_torrent.modelhub.downloadRepos as downloadRepos
import ptm_torrent.modelhub.setupFileSystem as setupFS

if __name__ == "__main__":
    setupFS.main()
    downloadJSON.main()
    downloadRepos.main()
    createSchema.main()
