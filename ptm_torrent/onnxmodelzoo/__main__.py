import ptm_torrent.onnxmodelzoo.downloadRepos as downloadRepos
import ptm_torrent.onnxmodelzoo.mdToHTML as mdToHTML
import ptm_torrent.onnxmodelzoo.setupFileSystem as setupFS

if __name__ == "__main__":
    setupFS.main()
    downloadRepos.main()
    mdToHTML.main()
    # downloadHubJSON.main()
    # downloadModelJSON.main()
    # createSchema.main()
