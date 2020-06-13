import products from "../pages/PublishedProducts";

export const state = () => ({
  products: [],
  product: null,
});

export const mutations = {
  loadProducts(state, payload) {
    const {products} = payload;
    console.log(products);
    state.products = products;
  },
  loadProduct(state, payload) {
    const {product} = payload;
    state.product = product;
  },

  updateComment(state, payload) {
    const {commentId, updatedComment} = payload;
    state.comments.splice(state.comments.findIndex(comment => comment.id === commentId), 1, updatedComment);
    console.log('updated comemnt', state.comments);
  },
  editProduct(state, payload) {
    const {productId, newProduct} = payload;
    console.log('mutations editProduct', productId, newProduct);
    state.products.splice(state.products.findIndex(product => product.id === productId), 1, newProduct);
  },
  deleteProduct(state, payload) {
    const {productId} = payload;
    state.product = null;
    state.products.splice(state.products.findIndex(product => product.id === productId), 1);
  }
};
export const actions = {

  loadAllProducts({commit}, paylaod) {
    return new Promise(async (resolve, reject) => {
      try {
        const res = await this.$axios.get(`http://127.0.0.1:8000/product/loadAllProducts`, {
          withCredentials: true
        });
        const {products} = res.data;
        commit('loadProducts', {products});
        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },

  /*-- load --*/
  loadPublishedProducts({commit}, payload) {
    return new Promise(async (resolve, reject) => {
        try {
          const res = await this.$axios.get(`http://127.0.0.1:8000/product/loadPublishedProducts`, {
            withCredentials: true
          });
          const {products} = res.data;
          commit('loadProducts', {products});
          return resolve();
        } catch (e) {
          console.error(e);
          return reject(e);
        }
      }
    )
  },

  loadNotPublishedProducts({commit}, payload) {
    return new Promise(async (resolve, reject) => {
        try {

          const res = await this.$axios.get(`http://127.0.0.1:8000/product/loadNotPublishedProducts`, {
            withCredentials: true
          });
          const {products} = res.data;
          commit('loadProducts', {products});
          return resolve();
        } catch (e) {
          console.error(e);
          return reject(e);
        }
      }
    )
  },

  loadProduct({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {productId} = payload;
        console.log('loadProduct productId', productId);
        const res = await this.$axios.get(`http://127.0.0.1:8000/product/loadProduct/${productId}`, {
          withCredentials: true
        });
        const {product} = res.data;
        commit('loadProduct', {product});
        return resolve();

      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },

  editProduct({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {productId} = payload;
        const res = await this.$axios.get(`http://127.0.0.1:8000/product/editProduct/${productId}`, {
          withCredentials: true
        });
        const {newProduct} = res.data;
        commit('editProduct', {productId, newProduct});
        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },

  deleteProduct({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {productId} = payload;
        await this.$axios.delete(`http://127.0.0.1:8000/product/deleteProduct/${productId}`, {
          withCredentials: true
        });
        commit('deleteProduct', {productId});
        return resolve();
      } catch (e) {
        console.error(e);
        return reject(e);
      }
    });
  },


};
