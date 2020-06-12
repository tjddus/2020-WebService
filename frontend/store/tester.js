export const state = () => ({
  tester: null,
  testers: [],
  averageGrade: '',});
export const mutations = {
  loadTesters(state, payload) {
    const {testers} = payload;
    state.testers = testers;
  },
  createTester(state, payload) {
    const {tester} = payload;
    state.tester = tester
    // state.testers.push(tester);
  },
  deleteTesters(state, payload) {
    const {productId} = payload;
    state.testers = [];
  }
};
export const actions = {
  loadTesters({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {productId} = payload;
        const res = await this.$axios.get(`http://127.0.0.1:8000/product/loadTesters/${productId}`, {
          withCredentials: true
        });
        const {testers} = res.data;
        console.log(testers);
        commit('loadTesters', {testers});
        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },
  createTester({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {productId, grade} = payload;
        const res = await this.$axios.post(`http://127.0.0.1:8000/product/createtester/${productId}`, {
          grade
        }, {
          withCredentials: true
        });
        const {tester} = res.data;
        commit('createTester', {tester});

        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },

  deleteTester({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {productId} = payload;
        await this.$axios.delete(`http://127.0.0.1:8000/product/deletetester/${productId}`, {
          withCredentials: true
        });
        commit('deleteTester', {productId});
        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  }
};
