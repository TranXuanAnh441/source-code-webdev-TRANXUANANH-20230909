<template>
    <h1>Trainings</h1>
    <hr /> <br />
    <h5 v-if="!trainings">No trainings yet</h5>
    <div v-else class="row">
        <div class="col-12 mb-3 mb-lg-5">
            <div class="position-relative card table-nowrap table-card">
                <div class="table-responsive">
                    <table class="table mb-0">
                        <thead class="small text-uppercase bg-body text-muted">
                            <tr>
                                <th>Training ID</th>
                                <th>Date</th>
                                <th>Author</th>
                                <th>Precision</th>
                                <th>Recall</th>
                                <th>Training Time(seconds)</th>
                                <th>Predicted result</th>
                                <th>Dataset</th>
                                <th>Model</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="training in trainings" :key="training.id" class="align-middle">
                                <td><router-link :to="{ name: 'Training', params: { id: training.id } }">#{{ training.id
                                }}</router-link></td>
                                <td>{{ training.created_at }}</td>
                                <td>{{ training.user.username }}</td>
                                <td>{{ training.precision }}</td>
                                <td>{{ training.recall }}</td>
                                <td>{{ training.training_time }}</td>
                                <td>{{ training.predicted_result }}</td>
                                <td><router-link :to="{ name: 'Dataset', params: { id: training.dataset } }">#{{
                                    training.dataset
                                }}</router-link></td>
                                <td>{{ training.model }}<router-link
                                        :to="{ name: 'Model', params: { id: training.training_model } }">#{{
                                            training.training_model
                                        }}</router-link></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
    name: 'Trainings',
    created: function () {
        return this.$store.dispatch('getTrainings');
    },
    computed: {
        ...mapGetters({ trainings: 'stateTrainings' }),
    },
});
</script>