<template>
  <div>
    <v-layout row justify-center>
      <v-dialog v-model="dialog" persistent max-width="500px">
        <v-form class="px-3" @submit.prevent="updateComment">
          <v-card>
            <v-card-title>
              <v-icon outlined>person_add</v-icon>
              <span class="headline-large-weight pl-4">댓글 수정</span>
            </v-card-title>
            <v-card-text>
              <v-container grid-list-md>
                <v-layout row wrap>
                  <v-flex xs20 sm20 md20>
                    <v-text-field filled v-model="newContent" box label="new content" class="caption"></v-text-field>
                    <small>*댓글 작성 시 비속어 유의합시다</small>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn type="submit" color="blue darken-3" flat @click="dialog = false" class="caption" dark>수정</v-btn>
              <v-btn color="blue darken-3" flat @click="dialog = false" class="caption" dark>닫기</v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>
    </v-layout>


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
              @click="updateCommentTrue(item)"
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
        dialog: false,
        headers: [
          {text: '아이디', align: 'left', sortable: 'false', value: 'user', width: '100px'},
          {text: '댓글', value: 'content', width: '200px'},
          {text: '수정', value: 'update', width: '30px'},
          {text: '삭제', value: 'delete', width: '30px'}
        ],
        currentComment: null,
        newContent: ''
      }
    },
    computed: {
      comments() {
        return this.$store.state.comment.comments;
      },
    },
    methods: {
      async deleteComment(item) {
        try {
          await this.$store.dispatch('comment/deleteComment', {
            commentId: item.id
          });
        } catch (e) {
          console.error(e);
        }
      },

      updateCommentTrue(item) {
        this.dialog = true;
        this.currentComment = item;
        console.log('click updateComment');
      },
      async updateComment() {
        try {
          console.log(this.currentComment);
          await this.$store.dispatch('comment/updateComment', {
            commentId: this.currentComment.id,
            newContent: this.newContent
          });
        } catch (e) {
          console.error(e);
        }
      }
    }
  }
</script>

<style scoped>

</style>
