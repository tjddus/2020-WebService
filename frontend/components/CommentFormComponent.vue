<template>
  <v-form v-model="valid" @submit.prevent="createComment">
    <v-container>
      <v-row justify="center">
        <v-col cols="8">
          <v-text-field
            v-model="content"
            label="content"
            :append-outer-icon="content? 'mdi-send':''"
            clear-icon="mdi-close-circle"
            clearable
            style="width: 560px"
            @click:append-outer="createComment"
            @click:clear="clearComment"
          >
          </v-text-field>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
  export default {
    name: "CommentFormComponent",
    data() {
      return {
        valid: false,
        content: ''
      }
    },
    props: {
      productId: ''
    },
    computed: {
      me() {
        return this.$store.state.user.me;
      }
    },
    methods: {
      clearComment() {
        this.content = ''
      },
      async createComment() {
        try {
          await this.$store.dispatch('comment/createComment', {
            content: this.content,
            productId: this.productId
          });
          this.clearComment();
        } catch (e) {
          console.error(e);
        }
      }
    }
  }
</script>

<style scoped>

</style>
