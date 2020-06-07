import products from "../pages/products";

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
  uploadProduct(state, payload) {
    const {product} = payload;
    state.products.push(product);
    state.imageUrls = [];
  },
  deleteProduct(state, payload) {
    const {productId} = payload;
    state.product = null;
    state.products.splice(state.products.findIndex(product => product.id === productId), 1);
  }
};
export const actions = {
  /*-- load --*/
  loadProducts({commit}, payload) {
    return new Promise(async (resolve, reject) => {
        try {

          const res = await this.$axios.get(`http://127.0.0.1:8000/product/loadProducts`, {
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
        console.log('loadproduct productId', productId);
        const res = await this.$axios.get(`http://127.0.0.1:8000/product/productDetail/${productId}`, {
          withCredentials: true
        });
        const {product} = res.data;
        commit('load{roduct', {product});
        return resolve();

      } catch (e) {
        console.error(e);
        return reject(e);
      }
    })
  },

  // *-- product --*
  uploadProduct({commit}, payload) {
    return new Promise(async (resolve, reject) => {
      try {
        const {title, content, imageUrls, tagNames} = payload;
        const res = await this.$axios.post('http://127.0.0.1:8000/product/createProduct', {
          title, content, imageUrls, tagNames
        }, {
          withCredentials: true
        });
        const {product} = res.data;
        commit('uploadProduct', {product});
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
        await this.$axios.delete(`http://localhost:4001/product/productDetail/${productId}`, {
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
