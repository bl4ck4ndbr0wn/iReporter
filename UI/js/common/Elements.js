const authForm = document.forms.auth_form;
const report_form = document.forms.report_form;
const profile_form = document.forms.profile_form;
const edit_incident_form = document.forms.edit_incident_form;
const edit_incident_status_form = document.forms.edit_incident_status_form;

const auth_register_elements = () => {
  const {
    auth_firstname,
    auth_lastname,
    auth_othername,
    auth_username,
    auth_email,
    auth_password,
    auth_confirm_password,
    register_submit
  } = authForm.elements;
  return {
    auth_firstname,
    auth_lastname,
    auth_othername,
    auth_username,
    auth_email,
    auth_password,
    auth_confirm_password,
    register_submit
  };
};

const auth_login_elements = () => {
  const { auth_username, auth_password, login_submit } = authForm.elements;
  return {
    auth_username,
    auth_password,
    login_submit
  };
};

const profile_elements = () => {
  const {
    auth_firstname,
    auth_lastname,
    auth_othername,
    auth_email,
    auth_phonenumber,
    profile_submit
  } = profile_form.elements;
  return {
    auth_firstname,
    auth_lastname,
    auth_othername,
    auth_email,
    auth_phonenumber,
    profile_submit
  };
};

const incident_record_elements = () => {
  const {
    title,
    record_type,
    comment,
    location,
    incident_submit
  } = report_form.elements;

  return {
    title,
    record_type,
    comment,
    location,
    incident_submit
  };
};

const edit_incident_elements = () => {
  const { comment, location } = edit_incident_form.elements;

  return {
    comment,
    location
  };
};

const edit_incident_status_elements = () => {
  const { status } = edit_incident_status_form.elements;

  return {
    status
  };
};
