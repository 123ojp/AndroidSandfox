<template>
  <div>
    <div class="jumbotron">
      <div class="container">
        <h1>任務列表</h1>
      </div>
    </div>
    <div class="col-md-12 offset-md-12">
      <div v-for="(value, name, index) in tasks">

        <h1 v-if="name=='pub'">Public Task</h1>
        <h1 v-if="name=='self'">Your Task</h1>
        <vue-good-table :columns="task_table" :rows="value" :sort-options="{
              enabled: true,
              initialSortBy: {field: 'app_id', type: 'desc'}
            }" :search-options="{
              enabled: true,
            }" :pagination-options="{
                enabled: true,
                mode: 'pages'
            }">
          <template slot="table-row" slot-scope="props">
            <span v-if="props.column.tags == 'func'">
              <router-link :to="{path: '/task/'+ props.row.app_id  }" class="btn btn-light" active-class="active" exac>
                <b-icon icon="arrow-right-circle-fill"></b-icon>
              </router-link>
            </span>
            <span v-else-if="props.column.tags == 'feature'">

              <span class="badge badge-primary">size:{{ parseInt(props.row.size/1024/1024) }}MB</span>
              <span class="badge badge-success">version:{{ props.row.androidversion_name }}</span>

              <span v-for="(item, index) in feature_list">
                <span v-if="props.row.hook_feature.includes(item)" class="badge badge-info">{{ item }}</span>
              </span>
              <span v-for="(item, index) in props.row.tags">
                <span class="badge badge-danger">{{ JSON.parse(item) }}</span>
              </span>
            </span>
            <span v-else-if="props.column.tags == 'icon'">
              <b-img fluid width="35px" class="round" :src="appicon+props.row.uuid+'.png'" alt="icon"  onerror="this.onerror=null;this.src='https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg';" ></b-img>
            </span>
            <span v-else-if="props.column.tags == 'state'">
              <span v-if="props.row.status>99" class="badge badge-secondary"> Finish </span>
              <span v-if="props.row.status<100&&props.row.status>2" class="badge badge-success"> Running </span>
              <span v-if="props.row.status<3" class="badge badge-warning"> Waiting </span>
            </span>
            <span v-else>
              {{props.formattedRow[props.column.field]}}
            </span>
          </template>
        </vue-good-table>
      </div>
    </div>
  </div>
</template>
<script>
  import {
    mapGetters,
    mapActions
  } from 'vuex'

  export default {

    data() {
      return {
        tasks: null,
        appicon: this.$HOST + "app/uploads/icon/",
        feature_list: ['IPC', 'Syscall', 'SQLiteDatabase', 'Native','SharedPreferences','mitm','BypassRoot'],
        task_table: [{
            label: 'ID',
            field: 'app_id',
            type: 'number',
            firstSortType: 'desc',
            width: '15px',
          },

          {
            label: "icon",
            field: "uuid",
            sortable: false,
            tags: 'icon',
            width: '15px',
          },
          {
            label: "State",
            field: "name",
            tags: 'state',
            width: '15px',
          },
          {
            label: "Name",
            field: "app_displayname",
            width: '100px',
          },
                    {
            label: 'Android id',
            field: 'name',
            width: '100px',

          },
          {
            label: 'Created On',
            field: 'created_date',
            formatFn: this.convertUnixTime,
            width: '100px',
          },
          {
            label: 'feature',
            field: 'hook_feature',
            tags: 'feature',
            sortable: false,
            width: '35%',
          },
          {
            label: '功能',
            field: 'app_id',
            tags: "func",
            sortable: false,
            width: '15px',

          }
        ]
      }
    },
    created: function () {
      this.getlist()
    },
    methods: {
      ...mapActions([
        'actionSetLoginInfo',
      ]),
      getlist() {
        var GETTASKS_API = this.$HOST + "app/list"
        this.$http.get(GETTASKS_API)
          .then((response) => {
            if (response.status == 200) {
              this.tasks = response.body.msg;
            } else {
              console.log(response.body)
              this.$swal("錯誤!", JSON.stringify(response.body), "error");
              localStorage.removeItem("token");
            }

          })
          .catch((response) => {
            this.$swal("錯誤!", JSON.stringify(response.body), "error");
          })
          .finally(() => {});
      },
      convertUnixTime(time) {
        let milliseconds = time * 1000
        let dateObject = new Date(milliseconds)
        return dateObject.toLocaleString()
      },
    },

  }

</script>
