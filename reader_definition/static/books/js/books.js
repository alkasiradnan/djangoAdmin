$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    console.log(btn.attr("data-url"))

    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-reader .modal-content").html("");
        $("#modal-reader").modal("show");
      },
      success: function (data) {
        console.log("hatmklamfd",data)
        $("#modal-reader .modal-content").html(data.html_form);
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
          $("#reader-table tbody").html(data.html_reader_definition_list);
          $("#modal-reader").modal("hide");
        }
        else {
          $("#modal-reader .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create reader
  $(".js-create-reader").click(loadForm);
  $("#modal-reader").on("submit", ".js-reader-create-form", saveForm);

  // Update reader
  $("#reader-table").on("click", ".js-update-reader", loadForm);
  $("#modal-reader").on("submit", ".js-reader-update-form", saveForm);

  // Delete reader
  $("#reader-table").on("click", ".js-delete-reader", loadForm);
  $("#modal-reader").on("submit", ".js-reader-delete-form", saveForm);

});
