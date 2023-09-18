<template>
    <section>
      <h1>Create new model</h1>
      <hr/> <br/>
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="description" class="form-label">Description:</label>
          <input type="text" name="description" v-model="model.description" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="train_test_split" class="form-label">train_test_split:</label>
          <input type="number" name="train_test_split" v-model="model.train_test_split" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="dropout_ratio" class="form-label">dropout_ratio:</label>
          <input type="number" name="dropout_ratio" v-model="model.dropout_ratio" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="layers_num" class="form-label">layers_num:</label>
          <input type="number" name="layers_num" v-model="model.layers_num" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
  </template>
  
  <script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'Create Model',
    data() {
      return {
        model: {
          description: '',
          train_test_split: 80,
          dropout_ratio: 10,
          layers_num: 3,
        },
      };
    },
    computed: {
      ...mapGetters({dataset: 'stateDataset' }),
    },
    methods: {
      ...mapActions(['createModel']),
      async submit() {
        const router = this.$router;
        try {
          await this.createModel(this.model).then(
            function response() { router.push('/models');}
          );
        } catch (error) {
          router.push('/error');
        }
      },
    },
  });
  </script>