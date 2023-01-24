# import ptm_torrent.huggingface.createSchema as createSchema
# import ptm_torrent.pytorchhub.downloadJSON as downloadJSON
# import ptm_torrent.pytorchhub.downloadRepos as downloadRepos
import ptm_torrent.pytorchhub.downloadModelList as downloadModelList
import ptm_torrent.pytorchhub.parseModelMetadata as parseModelMetadata
import ptm_torrent.pytorchhub.setupFileSystem as setupFS

if __name__ == "__main__":
    setupFS.main()
    downloadModelList.main()
    parseModelMetadata.main()
    # createSchema.main()
