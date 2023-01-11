#!/bin/bash

./0_setupScripts.bash
./1_setupHFTorrent.bash
./2_downloadUserList.bash
./3_downloadOrganizationPages.bash
./4_getModelMetadata.bash
./5_createUserData.bash
./6_gitCloneModels.bash
