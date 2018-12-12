const authForm = document.forms.auth_form;
const {
  auth_firstname,
  auth_lastname,
  auth_othername,
  auth_username,
  auth_email,
  auth_password,
  auth_confirm_password,
  submit
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
    submit
  };
};

export { auth_register_elements };
