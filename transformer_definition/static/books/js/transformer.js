$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-transformer .modal-content").html("");
        $("#modal-transformer").modal("show");
      },
      success: function (data) {
        console.log("hatmklamfd",data)
        $("#modal-transformer .modal-content").html(data.html_form);
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
          $("#transformer-table tbody").html(data.html_transformer_definition_list);
          $("#modal-transformer").modal("hide");
        }
        else {
          $("#modal-transformer .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create transformer
  $(".js-create-transformer").click(loadForm);
  $("#modal-transformer").on("submit", ".js-transformer-create-form", saveForm);

  // Update transformer
  $("#transformer-table").on("click", ".js-update-transformer", loadForm);
  $("#modal-transformer").on("submit", ".js-transformer-update-form", saveForm);

  // Delete transformer
  $("#transformer-table").on("click", ".js-delete-transformer", loadForm);
  $("#modal-transformer").on("submit", ".js-transformer-delete-form", saveForm);

});
