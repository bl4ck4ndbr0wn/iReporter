const authForm = document.forms.auth_form;
const {
  auth_firstname,
  auth_lastname,
  auth_othername,
  auth_username,
  auth_email,
  auth_password,
  auth_confirm_password,
  login_submit,
  register_submit
} = authForm.elements;

const auth_register_elements = () => {
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
  return {
    auth_username,
    auth_password,
    login_submit
  };
};
