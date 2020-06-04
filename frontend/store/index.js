import Cookie from 'js-cookie';

export const state = () => ({});
export const mutations = {};
export const actions = {
  async nuxtServerInit({dispatch}, {req}) {
    try {
      const cookie = req.headers.cookie.split('=')[1];
      console.log(cookie);
      await dispatch('user/loadMe', {cookie});
      // await dispatch('post/loadPosts', {reset: true});
      // await dispatch('waitingRoom/loadChatMe');
    } catch (e) {
      console.error(e);
    }
  }
};
