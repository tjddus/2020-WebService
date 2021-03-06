export const state = () => ({
  comments: []
});
export const mutations = {
  loadComments(state, payload) {
    const {comments} = payload;
    state.comments = comments;
  },
  createComment(state, payload) {
    const {comment} = payload;
    state.comments.push(comment);
  },
  updateComment(state, payload) {
    const {commentId, updatedComment} = payload;
    state.comments.splice(state.comments.findIndex(comment => comment.id === commentId), 1, updatedComment);
    console.log('updated comemnt', state.comments);
  },
  deleteComment(state, payload) {
    const {commentId} = payload;
    state.comments.splice(state.comments.findIndex(comment => comment.id === commentId), 1);
  }
};
export const actions = {
  loadComments({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {productId} = payload;
        const res = await this.$axios.get(`http://127.0.0.1:8000/product/loadComments/${productId}`, {
          withCredentials: true
        });
        const {comments} = res.data;
        console.log(comments);
        commit('loadComments', {comments});
        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },
  createComment({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {productId, content} = payload;
        const res = await this.$axios.post(`http://127.0.0.1:8000/product/createComment/${productId}`, {
          content
        }, {
          withCredentials: true
        });
        const {comment} = res.data;
        commit('createComment', {comment});

        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },
  updateComment({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {commentId, newContent} = payload;
        const res = await this.$axios.post(`http://127.0.0.1:8000/product/updateComment/${commentId}`, {
          newContent
        }, {
          withCredentials: true
        });
        const {updatedComment} = res.data;
        commit('updateComment', {commentId, updatedComment});
        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },
  deleteComment({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {commentId} = payload;
        await this.$axios.delete(`http://127.0.0.1:8000/product/deleteComment/${commentId}`, {
          withCredentials: true
        });
        commit('deleteComment', {commentId});
        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  }
};
