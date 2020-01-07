$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-writer .modal-content").html("");
        $("#modal-writer").modal("show");
      },
      success: function (data) {
        console.log("hatmklamfd",data)
        $("#modal-writer .modal-content").html(data.html_form);
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
          $("#writer-table tbody").html(data.html_writer_definition_list);
          $("#modal-writer").modal("hide");
        }
        else {
          $("#modal-writer .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create writer
  $(".js-create-writer").click(loadForm);
  $("#modal-writer").on("submit", ".js-writer-create-form", saveForm);

  // Update writer
  $("#writer-table").on("click", ".js-update-writer", loadForm);
  $("#modal-writer").on("submit", ".js-writer-update-form", saveForm);

  // Delete writer
  $("#writer-table").on("click", ".js-delete-writer", loadForm);
  $("#modal-writer").on("submit", ".js-writer-delete-form", saveForm);

});
