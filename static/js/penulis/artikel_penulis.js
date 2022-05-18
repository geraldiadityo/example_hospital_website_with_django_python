$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-penulis").modal("show");
            },
            success:function(data){
                $("#modal-penulis .modal-content").html(data.html_form);
            },
        });
    };

    var saveForm = function(){
        var form = $(this);
        $.ajax({
            url:form.attr("action"),
            type:form.attr("method"),
            data:form.serialize(),
            dataType:"JSON",
            cache:false,
            success:function(data){
                if (data.form_is_valid){
                    alert("data success sender!");
                    $("#table-artikel tbody").html(data.html_artikel_list);
                    $("#modal-penulis").modal("hide");
                }
                else{
                    $("#modal-penulis .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $(".js-create-artikel").click(loadForm);
    $("#modal-penulis").on("submit",".js-artikel-create-form",saveForm);
    $("#table-artikel tbody").on("click",".js-artikel-edit",loadForm);
    $("#modal-penulis").on("submit",".js-artikel-update-form",saveForm);
    $("#table-artikel tbody").on("click",".js-artikel-delete",loadForm);
    $("#modal-penulis").on("submit",".js-artikel-delete-form",saveForm);

});