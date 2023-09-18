<template>
  <section>
    <h1>Training details</h1>
    <hr /> <br />
    <div v-if="training">
      <p><strong>Author:</strong> {{ training.user.username }}</p>
      <p><strong>Precision:</strong> {{ training.precision }}</p>
      <p><strong>Recall:</strong> {{ training.recall }}</p>
      <p><strong>Predicted Result:</strong> {{ training.predicted_result }}</p>
      <p><strong>Training Time:</strong> {{ training.training_time }}</p>
      <br />
      <h2>Dataset & model </h2>
      <hr />
      <div class="datasets models row row-cols-md-5">
        <DatasetListItem :dataset="training.dataset" v-if="training.dataset"/>
        <ModelListItem :m="training.training_model" v-if="training.training_model"/>
      </div>
      <!-- <li><router-link :to="{ name: 'Create Model', params: { id: dataset.id } }">Create Model</router-link></li> -->
    </div>
  </section>
</template>
  
<style scoped>
.card {
  margin-right: 20px;
}
</style>
  
<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';
import ModelListItem from '@/components/ModelListItem.vue';
import DatasetListItem from '../../components/DatasetListItem.vue';

export default defineComponent({
  name: 'Training',
  components: {
    ModelListItem,
    DatasetListItem
  },
  props: ['id'],
  async created() {
    try {
      await this.viewTraining(this.$route.params.id);
    } catch (error) {
      this.$router.push('/error');
    }
  },
  computed: {
    ...mapGetters({ training: 'stateTraining', user: 'stateTraining' }),
  },
  methods: {
    ...mapActions(['viewTraining']),
  },
});
</script>