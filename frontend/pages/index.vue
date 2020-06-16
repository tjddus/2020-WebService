<template>
  <div>
    <div v-if="me">
      <account-card-component/>
    </div>
    <div v-else>
      <div align="center">
        <div>로그인하고 오세요</div>
        <div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import AccountCardComponent from "../components/AccountCardComponent";


  export default {
    name: "home",
    data() {
      return {}
    },
    components: {
      AccountCardComponent
    },
    computed: {
      me() {
        return this.$store.state.user.me;
      }
    }
  }
</script>

