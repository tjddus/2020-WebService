<template>
  <div>
    <v-layout justify-center="center" class="my-10">
      <v-flex xs12 md10>
        <v-toolbar-title class="font-weight-bold">댓글</v-toolbar-title>
        <v-data-table
          :headers="headers"
          :items="comments"
          hide-default-footer>

          <template v-slot:item.update="{item}">
            <v-icon
              small
              @click="updateComment(item)"
            >
              mdi-update
            </v-icon>
          </template>
          <template v-slot:item.delete="{ item }">
            <v-icon
              small
              @click="deleteComment(item)"
            >
              mdi-delete
            </v-icon>
          </template>

        </v-data-table>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
  export default {
    name: "CommentCardComponent",
    data() {
      return {
        headers: [
          {text: '아이디', align: 'left', sortable: 'false', value: 'user', width: '100px'},
          {text: '댓글', value: 'content', width: '200px'},
          {text: '수정', value: 'update', width: '30px'},
          {text: '삭제', value: 'delete', width: '30px'}
        ],
      }
    },
    computed: {
      comments() {
        return this.$store.state.comment.comments;
      },
    },
    methods: {
      async deleteComment() {
        try {
          await this.$store.dispatch('comment/deleteComment', {
            commentId: this.comment.id
          });
        } catch (e) {
          console.error(e);
        }
      },
      updateCommentTrue() {
        this.updateTrue = !this.updateTrue;
        this.newContent = this.comment.content;
        console.log('click updateComment');
      },
      async updateComment() {
        try {
          await this.$store.dispatch('comment/updateComment', {
            commentId: this.comment.id,
            newContent: this.newContent
          });
          this.updateTrue = false;
        } catch (e) {
          console.error(e);
        }
      }
    }
  }
</script>

<style scoped>

</style>
