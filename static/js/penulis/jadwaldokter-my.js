$(function(){
    var loadForm = function(){
        var btn = $(this);
        $.ajax({
            url:btn.attr("data-url"),
            type:"GET",
            dataType:"JSON",
            beforeSend:function(){
                $("#modal-jadwaldokter").modal("show");
            },
            success:function(data){
                $("#modal-jadwaldokter .modal-content").html(data.html_form);
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
            success:function(data){
                if (data.form_is_valid){
                    alert("data success sender!");
                    $("#table-jadwaldokter tbody").html(data.html_jadwal_list);
                    $("#modal-jadwaldokter").modal("hide");
                }
                else{
                    $("#modal-jadwaldokter .modal-content").html(data.html_form);
                }
            },
        });
        return false;
    };

    $(".js-jadwal-add").click(loadForm);
    $("#modal-jadwaldokter").on("submit",".js-jadwal-add-form",saveForm);
    $("#table-jadwaldokter tbody").on("click",".js-jadwal-edit",loadForm);
    $("#modal-jadwaldokter").on("submit",".js-jadwal-edit-form",saveForm);
    $("#table-jadwaldokter tbody").on("click",".js-jadwal-delete",loadForm);
    $("#modal-jadwaldokter").on("submit",".js-jadwal-delete-form",saveForm);
});