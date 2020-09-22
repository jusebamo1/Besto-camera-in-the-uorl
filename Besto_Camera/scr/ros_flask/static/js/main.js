$(document).ready(function() {
  $('.wButton').on('click', function() {
    $.ajax({
      type: 'POST',
      url: "/commands",
      data: {
        command: "w",
        linealVel : $('#linearVel').val(),
        angularVel : $('#angularVel').val()
      },
      dataType: "text",
    });
  });
  $('.aButton').on('click', function() {
    $.ajax({
      type: 'POST',
      url: "/commands",
      data: {
        command: "a",
        linealVel : $('#linearVel').val(),
        angularVel : $('#angularVel').val()
      },
      dataType: "text",
    });
  });
  $('.sButton').on('click', function() {
    $.ajax({
      type: 'POST',
      url: "/commands",
      data: {
        command: "s",
        linealVel : $('#linearVel').val(),
        angularVel : $('#angularVel').val()
      },
      dataType: "text",
    });
  });
  $('.dButton').on('click', function() {
    $.ajax({
      type: 'POST',
      url: "/commands",
      data: {
        command: "d",
        linealVel : $('#linearVel').val(),
        angularVel : $('#angularVel').val()
      },
      dataType: "text",
    });
  });
  $('.stopButton').on('click', function() {
    $.ajax({
      type: 'POST',
      url: "/commands",
      data: {
        command: "stop",
        linealVel : $('#linearVel').val(),
        angularVel : $('#angularVel').val()
      },
      dataType: "text",
    });
  });
  var delay = 1 * 1000;
  var intervalID = setInterval(update_values, delay);
  var xVal = 0;
  var dataLength = 20;
  var count = 0
  var illu = []; // dataPoints
  var chartillu = new CanvasJS.Chart("illuminance_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Illuminance Data"
    },
    data: [{
      type: "line",
      dataPoints: illu
    }]
  });
  var imuox = [],
    imuoy = [],
    imuoz = [],
    imuax = [],
    imuay = [],
    imuaz = [],
    imulx = [],
    imuly = [],
    imulz = [],
    mfx = [],
    mfy = [],
    mfz = [];
  var chartImuox = new CanvasJS.Chart("imuox_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Orientation X"
    },
    data: [{
      type: "line",
      dataPoints: imuox
    }]
  });
  var chartImuoy = new CanvasJS.Chart("imuoy_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Orientation Y"
    },
    data: [{
      type: "line",
      dataPoints: imuoy
    }]
  });
  var chartImuoz = new CanvasJS.Chart("imuoz_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Orientation Z"
    },
    data: [{
      type: "line",
      dataPoints: imuoz
    }]
  });
  var chartImuax = new CanvasJS.Chart("imuax_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Angular Velocity X"
    },
    data: [{
      type: "line",
      dataPoints: imuax
    }]
  });
  var chartImuay = new CanvasJS.Chart("imuay_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Angular Velocity Y"
    },
    data: [{
      type: "line",
      dataPoints: imuay
    }]
  });
  var chartImuaz = new CanvasJS.Chart("imuaz_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Angular Velocity Z"
    },
    data: [{
      type: "line",
      dataPoints: imuaz
    }]
  });
  var chartImulx = new CanvasJS.Chart("imulx_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Linear Acceleration X"
    },
    data: [{
      type: "line",
      dataPoints: imulx
    }]
  });
  var chartImuly = new CanvasJS.Chart("imuly_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Linear Acceleration Y"
    },
    data: [{
      type: "line",
      dataPoints: imuly
    }]
  });
  var chartImulz = new CanvasJS.Chart("imulz_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Linear Acceleration Z"
    },
    data: [{
      type: "line",
      dataPoints: imulz
    }]
  });
  var chartMfx = new CanvasJS.Chart("mfx_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Magnetic Field X"
    },
    data: [{
      type: "line",
      dataPoints: mfx
    }]
  });
  var chartMfy = new CanvasJS.Chart("mfy_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Magnetic Field Y"
    },
    data: [{
      type: "line",
      dataPoints: mfy
    }]
  });
  var chartMfz = new CanvasJS.Chart("mfz_chart", {
    animationEnabled: true,
    theme: "dark2",
    title: {
      text: "Magnetic Field Z"
    },
    data: [{
      type: "line",
      dataPoints: mfz
    }]
  });

  function update_values() {
    $.getJSON('/data',
      function(data) {
        $('#illuminance_data').text(data.illu_data);
        $('#imuox').text(data.imu_ox);
        $('#imuoy').text(data.imu_oy);
        $('#imuoz').text(data.imu_oz);
        $('#imuavx').text(data.imu_vax);
        $('#imuavy').text(data.imu_vay);
        $('#imuavz').text(data.imu_vaz);
        $('#imulax').text(data.imu_lax);
        $('#imulay').text(data.imu_lax);
        $('#imulaz').text(data.imu_lax);
        $('#mfx').text(data.mfx);
        $('#mfy').text(data.mfy);
        $('#mfz').text(data.mfz);
        count = count || 1;
        for (var j = 0; j < count; j++) {
          illu.push({
            x: xVal,
            y: data.illu_data
          });
          imuox.push({
            x: xVal,
            y: data.imu_ox
          });
          imuoy.push({
            x: xVal,
            y: data.imu_oy
          });
          imuoz.push({
            x: xVal,
            y: data.imu_oz
          });
          imuax.push({
            x: xVal,
            y: data.imu_vax
          });
          imuay.push({
            x: xVal,
            y: data.imu_vay
          });
          imuaz.push({
            x: xVal,
            y: data.imu_vaz
          });
          imulx.push({
            x: xVal,
            y: data.imu_lax
          });
          imuly.push({
            x: xVal,
            y: data.imu_lay
          });
          imulz.push({
            x: xVal,
            y: data.imu_laz
          });
          mfx.push({
            x: xVal,
            y: data.mfx
          });
          mfy.push({
            x: xVal,
            y: data.mfy
          });
          mfz.push({
            x: xVal,
            y: data.mfz
          });
          xVal++;
        }
        if (illu.length > dataLength) {
          illu.shift();
        }
        chartillu.render();
        chartImuox.render();
        chartImuoy.render();
        chartImuoz.render();
        chartImuax.render();
        chartImuay.render();
        chartImuaz.render();
        chartImulx.render();
        chartImuly.render();
        chartImulz.render();
        chartMfx.render();
        chartMfy.render();
        chartMfz.render();
      });
  };
});
