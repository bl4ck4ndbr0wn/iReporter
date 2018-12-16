const authForm = document.forms.auth_form;
const report_form = document.forms.report_form;

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
