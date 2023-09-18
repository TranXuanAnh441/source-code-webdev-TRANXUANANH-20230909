<template>
  <section>
    <h1>Dataset details</h1>
    <hr /> <br />
    <div v-if="dataset">
      <p><strong>Title:</strong> {{ dataset.title }}</p>
      <p><strong>Description:</strong> {{ dataset.description }}</p>
      <p><strong>Author:</strong> {{ dataset.user.username }}</p>
      <div v-if="user.role === 'admin'" class="mt-3 md-2">
        <p><button @click="removeDataset()" class="btn btn-primary">Delete Dataset</button></p>
      </div>
      <br />

      <section>
        <h2>Dataset files</h2>
        <div class="d-flex" v-if="user.id===dataset.user.id">
          <div class="input-group w-auto">
            <input type="file" class="form-control col-lg-5" @change="handleFileUpload($event)" />
            <button class="btn btn-primary" @click="submitFile()" data-mdb-ripple-color="dark">Upload file</button>
          </div>
        </div>
        <hr /><br />
        <h5 v-if="!dataset.files">No files yet</h5>
        <div v-else class="files row row-cols-1 row-cols-md-5">
          <div v-for="file in dataset.files" :key="file.id" class="files">
            <div class="card rounded-6">
              <img
                src="https://www.lifewire.com/thmb/inNQyGnr7uhFU2sfegkjjv0mh9Q=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/csv-file-icon-a7f3994552eb4499afb3f3cf57c59adc.jpg"
                class="card-img-top mt-2">
              <div class="card-body">
                <a @click="download(file.id)" class="btn text-primary">{{ file.name }}</a>
              </div>
              </div>
            </div>
          </div>
      </section>
      <br />

      <h2>Train this dataset with models</h2>
      <hr />
      <div v-if="!models">No models</div>
      <div v-else class="models row row-cols-1 row-cols-md-5">
        <div v-for="model in models" :key="model.id" class="models">
          <a @click="modelTrain(model.id)" class="btn text-primary">Train this model</a>
          <ModelListItem :m="model"/>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.models {
  height: 80%;
}
</style>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';
import ModelListItem from '@/components/ModelListItem.vue';

export default defineComponent({
  name: 'Dataset',
  components: {
    ModelListItem,
  },
  data() {
    return {
      file: ''
    }
  },
  props: ['id'],
  async created() {
    try {
      await this.viewDataset(this.$route.params.id);
      await this.$store.dispatch('getModels');
    } catch (error) {
      this.$router.push('/error');
    }
  },
  computed: {
    ...mapGetters({ dataset: 'stateDataset', models: 'stateModels', user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['viewDataset', 'deleteDataset', 'uploadFile', 'downloadFile', 'createTraining']),
    async removeDataset() {
      await this.deleteDataset(this.$route.params.id);
      this.$router.push('/datasets');
    },
    async modelTrain(model_id) {
      const router = this.$router;
      try {
        const training = {
          note: 'note about this training result',
          precision: 0,
          recall: 1,
          predicted_result: 0,
          training_time: 10,
          dataset: this.$route.params.id,
          training_model: model_id,
        }
        await this.createTraining(training).then (
          function response() {
            router.push('/trainings');
          }
        );
      } catch (error) {
        console.log(error);
        this.$router.push('/error');
      }
    },
    handleFileUpload(event) {
      this.file = event.target.files[0];
      // console.log(this.file);
    },
    async submitFile() {
      let formData = new FormData();
      formData.append('dataset', this.$route.params.id);
      formData.append('file', this.file);

      await this.uploadFile(formData);
      this.$router.go(this.$router.currentRoute);
    },
    async download(file_id) {
      console.log(file_id);
      await this.downloadFile(file_id);
    }
  },
});
</script>