<template>
  <section>
    <h1>Model details</h1>
    <hr /> <br />
    <div v-if="model">
      <p><strong>Description:</strong> {{ model.description }}</p>
      <p><strong>Author:</strong> {{ model.user.username }}</p>
      <p><strong>train_test_split:</strong> {{ model.train_test_split }}</p>
      <p><strong>dropout_ratio:</strong> {{ model.dropout_ratio }}</p>
      <p><strong>layers_num:</strong> {{ model.layers_num }}</p>
      <div v-if="user.role==='admin'">
        <p><button @click="removeModel()" class="btn btn-primary">Delete Model</button></p>
      </div>
      <br/>
      <h2>Trainings</h2>
      <hr /> <br />
      <h5 v-if="!model.training_results.length">No trainings yet</h5>
      <div v-else class="row">
        <div class="col-12 mb-3 mb-lg-5">
          <div class="position-relative card table-nowrap table-card">
            <div class="table-responsive">
              <table class="table mb-0">
                <thead class="small text-uppercase bg-body text-muted">
                  <tr>
                    <th>Training ID</th>
                    <th>Date</th>
                    <th>Precision</th>
                    <th>Recall</th>
                    <th>Training time (seconds)</th>
                    <th>Predicted value</th>
                  </tr>
                </thead>

                <tbody>
                  <tr v-for="training in model.training_results" :key="training.id" class="align-middle">
                    <td><router-link :to="{ name: 'Training', params: { id: training.id } }">#{{ training.id }}</router-link></td>
                    <td>{{ training.created_at }}</td>
                    <td>{{ training.precision }}</td>
                    <td>{{ training.recall }}</td>
                    <td>{{ training.training_time }}</td>
                    <td>
                      <span class="badge fs-6 fw-normal bg-tint-success text-success">{{ training.predicted_result
                      }}</span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="card-footer text-end">
              <!-- <a @click="modelTrain" class="btn btn-gray">Train this model</a> -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.avatar.sm {
  width: 2.25rem;
  height: 2.25rem;
  font-size: .818125rem;
}

.table-nowrap .table td,
.table-nowrap .table th {
  white-space: nowrap;
}

.table>:not(caption)>*>* {
  padding: 0.75rem 1.25rem;
  border-bottom-width: 1px;
}

table th {
  font-weight: 600;
  background-color: #eeecfd !important;
}
</style>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Model',
  props: ['id'],
  async created() {
    try {
      await this.viewModel(this.id);
    } catch (error) {
      this.$router.push('/error');
    }
  },
  computed: {
    ...mapGetters({ model: 'stateModel', user: 'stateUser' }),
  },
  methods: {
    ...mapActions(['viewModel', 'deleteModel', 'createTraining']),
    async modelTrain() {
      try {
        const training = {
          note: 'note about this training result',
          precision: 0,
          recall: 1,
          predicted_result: 0,
          training_time: 10,
          training_model: this.$route.params.id
        }
        await this.createTraining(training);
        this.$router.push({ name: 'Model', params: { id: this.$route.params.id } });
      } catch (error) {
        this.$router.push('/error');
      }
    },
    async removeModel() {
      try {
        await this.deleteModel(this.$route.params.id);
        this.$router.push('/models');
      } catch(error) {
        this.$router.push('/error');
      }
    }
  },
});
</script>
