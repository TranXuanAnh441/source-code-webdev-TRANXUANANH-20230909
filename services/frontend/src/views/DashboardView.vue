<template>
  <section>
    <h1 v-if="user">Welcome back {{ user.username }}</h1>
    <br />
  </section>

    <section>
    <h2> Your Datasets</h2>
    <hr /><br />
    <h5 v-if="datasets==null">You have no datasets yet</h5>
    <div v-else class="datasets row row-cols-1 row-cols-md-5">
      <template v-for="dataset in datasets" :key="dataset.id">
        <DatasetListItem :dataset="dataset" v-if="user && dataset.user.id === user.id" />
      </template>
    </div>
  </section>

  <section>
    <h2>Your Models</h2>
    <hr /><br />
    <h5 v-if="!models">You have no models yet</h5>
    <div v-else class="models row row-cols-1 row-cols-md-5">
      <template v-for="m in models" :key="m.id">
        <ModelListItem :m="m" v-if="user && m.user.id === user.id"/>
      </template>
    </div>
  </section>
</template>

<style scoped>
.card {
  margin-left: 15px;
}

</style>
<script >
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';
import ModelListItem from '@/components/ModelListItem.vue';
import DatasetListItem from '@/components/DatasetListItem.vue';

export default defineComponent({
  name: 'DashBoard',
  components: {
    ModelListItem,
    DatasetListItem
  },
  created: async function () {
      await this.$store.dispatch('getDatasets');
      await this.$store.dispatch('getModels');
  },
  computed: {
    ...mapGetters({ datasets: 'stateDatasets', models: 'stateModels', user: 'stateUser' }),
  },
});
</script>