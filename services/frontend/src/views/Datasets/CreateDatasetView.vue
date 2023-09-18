<template>
  <section>
    <h1>Create Datasets</h1>
    <hr /> <br />
    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="title" class="form-label">Dataset Title:</label>
        <input type="text" name="title" v-model="dataset.title" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Description:</label>
        <input type="text" name="description" v-model="dataset.description" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Create Dataset',
  data() {
    return {
      dataset: {
        title: '',
        description: '',
        image: 'default'
      },
    };
  },
  computed: {
    ...mapGetters({ user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['createDataset']),
    async submit() {
      const router = this.$router;
      try {
        await this.createDataset(this.dataset).then(
          function response() { router.push('/datasets'); }
        );
      } catch (error) {
        router.push('/error');
      }
    },
  },
});
</script>