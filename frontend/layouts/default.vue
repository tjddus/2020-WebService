<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      width="13%"
    >
      <v-list dense>
        <v-list-item v-for="item in items" :key="item.title" router :to="item.route">
          <v-list-item-action :to="item.to">
            <v-icon>{{item.icon}}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{item.title}}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
      :height="55"
      color="primary"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title small class="font-weight-bold">WADIZ IMPROVEMENT</v-toolbar-title>
      <v-spacer/>
      <v-btn icon class="mr-2" nuxt to="inspire">
        <v-icon flat small>person</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <nuxt/>
    </v-content>

    <v-footer app>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
  import 'material-design-icons-iconfont/dist/material-design-icons.css'

  export default {
    props: {
      source: String,
    },
    data() {
      return {
        drawer: null,
        items: [
          {title: 'WADIZ', icon: 'school', route: '/'},
          {title: '내 파일', icon: 'folder', route: '/'},
          {title: '심사상품목록', icon: 'list', route: '/NotPublishedProducts'},
          {title: '상품목록', icon: 'image', route: '/PublishedProducts'},
        ]
      }
    }
  }
</script>

<style scoped>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
