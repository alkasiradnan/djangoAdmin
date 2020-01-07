$(function () {

  /* Functions */

  var loadForm = function () {
    console.log("iconnect")
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-operation .modal-content").html("");
        $("#modal-operation").modal("show");
      },
      success: function (data) {
        console.log("hatmklamfd",data)
        $("#operation-list").html(data.html_form);
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
          $("#operation-table tbody").html(data.html_operation_list);
          $("#modal-operation").modal("hide");
        }
        else {
          $("#modal-operation .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */
loadForm();
  // Create operation
  $(".js-create-operation").click(loadForm);
  $("#modal-operation").on("submit", ".js-operation-create-form", saveForm);

  // Update operation
  $("#operation-table").on("click", ".js-update-operation", loadForm);
  $("#modal-operation").on("submit", ".js-operation-update-form", saveForm);

  // Delete operation
  $("#operation-table").on("click", ".js-delete-operation", loadForm);
  $("#modal-operation").on("submit", ".js-operation-delete-form", saveForm);

});
