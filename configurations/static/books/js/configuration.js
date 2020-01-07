$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-configuration .modal-content").html("");
        $("#modal-configuration").modal("show");
      },
      success: function (data) {
        console.log("hatmklamfd",data)
        $("#modal-configuration .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        console.log(data)
        if (data.form_is_valid) {
          $("#configuration-table tbody").html(data.html_configuration_list);
          $("#modal-configuration").modal("hide");
        }
        else {
          $("#modal-configuration .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create configuration
  $(".js-create-configuration").click(loadForm);
  $("#modal-configuration").on("submit", ".js-configuration-create-form", saveForm);

  // Update configuration
  $("#configuration-table").on("click", ".js-update-configuration", loadForm);
  $("#modal-configuration").on("submit", ".js-configuration-update-form", saveForm);

  // Delete configuration
  $("#configuration-table").on("click", ".js-delete-configuration", loadForm);
  $("#modal-configuration").on("submit", ".js-configuration-delete-form", saveForm);

});
