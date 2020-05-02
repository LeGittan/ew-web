Vue.filter('currency', function(value) {
  return  value.toFixed(2) + ' EUR';
});

  var app = new Vue ({
  el: "#calc",
  data () {
    return {
      services: null
    }
  },
  mounted () {
    axios
      .get('https://legittan-ew-web-master-1072939.dev.odoo.com/api/apps')
      .then(response => (this.services = response.data))
      console.log(this.services)
  },
  methods: {
    toggleActive: function(s) {
      s.active = !s.active;
    },
    total: function() {
      var total = 0;      
      this.services.forEach(function(s) {
        if (s.active) {
          total += s.price_per_month;
        }
      });
      return total;
    },
    countApps: function() {
      var countApps = 0;      
      this.services.forEach(function(s) {
        if (s.active) {
          countApps = countApps +1;
          
        }
      });
      return countApps;
    }
  }
});