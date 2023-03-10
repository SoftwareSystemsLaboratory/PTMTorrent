import ptm_torrent.onnxmodelzoo.createSchema as createSchema
import ptm_torrent.onnxmodelzoo.downloadRepos as downloadRepos
import ptm_torrent.onnxmodelzoo.mdToHTML as mdToHTML
import ptm_torrent.onnxmodelzoo.parseHubHTML as parseHub
import ptm_torrent.onnxmodelzoo.parseModelHTML as parseModels
import ptm_torrent.onnxmodelzoo.setupFileSystem as setupFS

if __name__ == "__main__":
    setupFS.main()
    downloadRepos.main()
    mdToHTML.main()
    parseHub.main()
    parseModels.main()
    createSchema.main()
