import ptm_torrent.pytorchhub.createSchema as createSchema
import ptm_torrent.pytorchhub.downloadModelList as downloadModelList
import ptm_torrent.pytorchhub.downloadRepos as downloadRepos
import ptm_torrent.pytorchhub.parseModelMetadata as parseModelMetadata
import ptm_torrent.pytorchhub.setupFileSystem as setupFS

if __name__ == "__main__":
    setupFS.main()
    downloadModelList.main()
    parseModelMetadata.main()
    downloadRepos.main()
    createSchema.main()
