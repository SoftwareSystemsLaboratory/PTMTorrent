import ptm_torrent.modelzoo.downloadHubJSON as downloadHubJSON
import ptm_torrent.modelzoo.setupFileSystem as setupFS

if __name__ == "__main__":
    setupFS.main()
    downloadHubJSON.main()
    # downloadRepos.main()
    # createSchema.main()
