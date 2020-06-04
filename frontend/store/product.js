export const state = () => ({
  files: [],
  file: null,
});

export const mutations = {
  loadFiles(state, payload) {
    const {files} = payload;
    state.files = files;
  },
  uploadFolder(state, payload) {
    const {file} = payload;
    console.log(file);
    state.files.push(file);
  },
  uploadFiles(state, payload) {
    const {files} = payload;
    state.files.concat(files);
  },
  deleteFile(state, payload) {
    const {fileId} = payload;
    state.file = null;
    state.files.splice(state.files.findIndex(file => file.id === fileId), 1);
  },
};

export const actions = {
  loadFiles({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await this.$axios.get('http://127.0.0.1:8000/files/loadFiles', {
          withCredentials: true
        });
        const {files} = res.data;
        commit('loadFiles', {files});
        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },
  uploadFolder({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        // const {formData} = payload;
        // const res = await this.$axios.post('http://127.0.0.1:8000/files/uploadFolder', formData, {
        //   withCredentials: true
        // });
        const {file} = payload;
        // const {file} = res;
        console.log(file);
        commit('uploadFolder', {file});
        return resolve();

      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },
  uploadFiles({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {formData} = payload;
        for (var value of formData.values()) {

          console.log(value);

        }
        const res = await this.$axios.post('http:/127.0.0.1:8000/files/uploadFiles', formData, {
          withCredentials: true
        });
        const {files} = res.data;
        commit('uploadFiles', files);
        return resolve();

      } catch (e) {
        console.error(e);
        return reject(e);
      }
    });
  },
  deleteFolder({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {folderId} = payload;
        await this.$axios.get('http://127.0.0.1/files/deleteFile', {
          fileId: folderId
        }, {
          withCredentials: true
        });
        commit('deleteFile', {fileId: folderId});

      } catch (e) {
        console.error(e);
        return reject(e);
      }
    });
  },
  deleteFile({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {fileId} = payload;
        await this.$axios.get('http://127.0.0.1/files/deleteFile', {
          fileId: fileId
        }, {
          withCredentials: true
        });
        commit('deleteFile', {fileId: fileId});

      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },
  // updateFolder({commit}, payload) {
  //
  // },
  // updateFile({commit}, payload) {
  //
  // }
};
