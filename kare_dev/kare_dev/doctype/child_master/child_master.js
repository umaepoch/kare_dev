// Copyright (c) 2021, Pavithra M R and contributors
// For license information, please see license.txt
frappe.require("/assets/kare_dev/js/camera.js")

var data = "data:image/png;base64,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"


frappe.ui.form.on("Images","activate_camera", function(frm, cdt, cdn){
  let images = { data: "reached api call!!!"}
  var doc = locals[cdt][cdn]
  let is_created;

  if (doc.image_name) {
    // show()
    // submit((data) => {
    //   let img = data.split(",")
    //   images.data = img[1]
    // })
    // images.data = data.split(",")[1]
    // images.image_name = doc.image_name
    // images.doc_name = doc.name
    // images.first_name = frm.doc.first_name
    // images.doctype = doc.doctype
    // console.log(images)
    is_created = create_image_url(JSON.stringify(images))

    // if (is_created) {
    //   doc.attach = is_created
    // }
  } else {
    frappe.throw(__("To activate camera enter image name"))
  }
});


// API for creating image url.
function create_image_url(doc) {
  let flag;
	frappe.call({
		method:'kare_dev.kare_dev.doctype.child_master.child_master.create_image_url',
		args: {
      'doc': doc
		},
		async: false,
		callback: function(r) {
			if(r.message){
				if (r.message.SC) {
          flag = r.message.file_url
        } else {
          frappe.throw(__(`Image URL creation failed`))
        }
        if (r.message.EX) {
          frappe.throw(__(r.message.EX))
        }
			}
		}
	})
  return flag
}

frappe.ui.form.on("Images", "form_render", function(frm, cdt, cdn){
  var doc = locals[cdt][cdn]
  // console.log(doc)

  if (frm.is_dirty()) {
    frm.save()
  }
  // console.log(frm.doc)
  if (doc.attach && !frm.is_dirty()) {
    var wrapper = frm.fields_dict[doc.parentfield].grid.grid_rows_by_docname[cdn].grid_form.fields_dict['image_preview'].$wrapper
    var is_viewable = frappe.utils.is_image_file(doc.attach);
    console.log(is_viewable)

    // frm.toggle_display("upload_section", is_viewable);
    frm.toggle_display("image_preview", is_viewable);

    if(is_viewable){
      wrapper.html('<div class="img_preview">\
      <img class="img-responsive" src="'+doc.attach+'"></img>\
      </div>');
    } else {
      wrapper.empty();
    }
  } else {
    var wrapper = frm.fields_dict[doc.parentfield].grid.grid_rows_by_docname[cdn].grid_form.fields_dict['image_preview'].$wrapper
    var is_viewable = frappe.utils.is_image_file(doc.attach);

    frm.toggle_display("image_preview", is_viewable);

    if (!is_viewable) {
      wrapper.empty();
    }
  }
})
