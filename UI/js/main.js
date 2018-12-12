/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./UI/js/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./UI/js/api/index.js":
/*!****************************!*\
  !*** ./UI/js/api/index.js ***!
  \****************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\nfunction _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError(\"Cannot call a class as a function\"); } }\n\nfunction _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if (\"value\" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }\n\nfunction _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }\n\nvar Api =\n/*#__PURE__*/\nfunction () {\n  function Api() {\n    _classCallCheck(this, Api);\n\n    this.apiURL = \"https://ireporter2018v2.herokuapp.com/api/v2\";\n  }\n\n  _createClass(Api, [{\n    key: \"logError\",\n    value: function logError(err) {\n      console.log(\"Looks like there was a problem: \\n\", error);\n    }\n  }, {\n    key: \"validateResponse\",\n    value: function validateResponse(resp) {\n      if (!response.ok) {\n        throw Error(response.statusText);\n      }\n\n      return response;\n    }\n  }, {\n    key: \"readResponseAsJSON\",\n    value: function readResponseAsJSON(resp) {\n      return resp.json();\n    }\n  }, {\n    key: \"get\",\n    value: function get(endpoint) {\n      var URL = \"\".concat(this.apiURL).concat(endpoint);\n      return fetch(URL, {\n        method: \"GET\",\n        mode: \"cors\",\n        cache: \"default\"\n      }).then(this.validateResponse).then(this.readResponseAsJSON).catch(this.logError);\n    }\n  }, {\n    key: \"post\",\n    value: function post(endpoint, data) {\n      var URL = \"\".concat(this.apiURL).concat(endpoint);\n      return fetch(URL, {\n        method: \"POST\",\n        mode: \"cors\",\n        headers: {\n          \"Content-Type\": \"application/json\"\n        },\n        body: JSON.stringify(data)\n      }).then(this.validateResponse).then(this.readResponseAsJSON).catch(this.logError);\n    }\n  }]);\n\n  return Api;\n}();\n\n/* harmony default export */ __webpack_exports__[\"default\"] = (Api);\n\n//# sourceURL=webpack:///./UI/js/api/index.js?");

/***/ }),

/***/ "./UI/js/common/App.js":
/*!*****************************!*\
  !*** ./UI/js/common/App.js ***!
  \*****************************/
/*! exports provided: Component */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"Component\", function() { return Component; });\nfunction _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError(\"Cannot call a class as a function\"); } }\n\nfunction _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if (\"value\" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }\n\nfunction _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }\n\nvar Component =\n/*#__PURE__*/\nfunction () {\n  function Component() {\n    _classCallCheck(this, Component);\n\n    this.setState = this.setState.bind(this);\n  }\n\n  _createClass(Component, [{\n    key: \"setState\",\n    value: function setState(newState) {\n      return Object.assign(this.state, newState);\n    }\n  }]);\n\n  return Component;\n}();\n\n//# sourceURL=webpack:///./UI/js/common/App.js?");

/***/ }),

/***/ "./UI/js/common/Elements.js":
/*!**********************************!*\
  !*** ./UI/js/common/Elements.js ***!
  \**********************************/
/*! exports provided: auth_register_elements */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, \"auth_register_elements\", function() { return auth_register_elements; });\nvar authForm = document.forms.auth_form;\nvar _authForm$elements = authForm.elements,\n    auth_firstname = _authForm$elements.auth_firstname,\n    auth_lastname = _authForm$elements.auth_lastname,\n    auth_othername = _authForm$elements.auth_othername,\n    auth_username = _authForm$elements.auth_username,\n    auth_email = _authForm$elements.auth_email,\n    auth_password = _authForm$elements.auth_password,\n    auth_confirm_password = _authForm$elements.auth_confirm_password,\n    submit = _authForm$elements.submit;\n\nvar auth_register_elements = function auth_register_elements() {\n  return {\n    auth_firstname: auth_firstname,\n    auth_lastname: auth_lastname,\n    auth_othername: auth_othername,\n    auth_username: auth_username,\n    auth_email: auth_email,\n    auth_password: auth_password,\n    auth_confirm_password: auth_confirm_password,\n    submit: submit\n  };\n};\n\n\n\n//# sourceURL=webpack:///./UI/js/common/Elements.js?");

/***/ }),

/***/ "./UI/js/components/Register.js":
/*!**************************************!*\
  !*** ./UI/js/components/Register.js ***!
  \**************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _common_App__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../common/App */ \"./UI/js/common/App.js\");\n/* harmony import */ var _common_Elements__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../common/Elements */ \"./UI/js/common/Elements.js\");\n/* harmony import */ var _api_index__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../api/index */ \"./UI/js/api/index.js\");\nfunction _typeof(obj) { if (typeof Symbol === \"function\" && typeof Symbol.iterator === \"symbol\") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === \"function\" && obj.constructor === Symbol && obj !== Symbol.prototype ? \"symbol\" : typeof obj; }; } return _typeof(obj); }\n\nfunction _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; var ownKeys = Object.keys(source); if (typeof Object.getOwnPropertySymbols === 'function') { ownKeys = ownKeys.concat(Object.getOwnPropertySymbols(source).filter(function (sym) { return Object.getOwnPropertyDescriptor(source, sym).enumerable; })); } ownKeys.forEach(function (key) { _defineProperty(target, key, source[key]); }); } return target; }\n\nfunction _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }\n\nfunction _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError(\"Cannot call a class as a function\"); } }\n\nfunction _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if (\"value\" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }\n\nfunction _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }\n\nfunction _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === \"object\" || typeof call === \"function\")) { return call; } return _assertThisInitialized(self); }\n\nfunction _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }\n\nfunction _inherits(subClass, superClass) { if (typeof superClass !== \"function\" && superClass !== null) { throw new TypeError(\"Super expression must either be null or a function\"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); if (superClass) _setPrototypeOf(subClass, superClass); }\n\nfunction _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf || function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }\n\nfunction _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError(\"this hasn't been initialised - super() hasn't been called\"); } return self; }\n\n\n\n\n\nvar Register =\n/*#__PURE__*/\nfunction (_Component) {\n  _inherits(Register, _Component);\n\n  function Register() {\n    var _this;\n\n    _classCallCheck(this, Register);\n\n    _this = _possibleConstructorReturn(this, _getPrototypeOf(Register).call(this));\n    _this.state = {\n      firstname: \"\",\n      lastname: \"\",\n      othernames: \"\",\n      email: \"\",\n      phoneNumber: \"\",\n      username: \"\",\n      password: \"\",\n      password_confirm: \"\",\n      errors: {}\n    };\n    _this.url = \"/auth/signup\";\n    _this.api = new _api_index__WEBPACK_IMPORTED_MODULE_2__[\"default\"]();\n    _this.elements = Object(_common_Elements__WEBPACK_IMPORTED_MODULE_1__[\"auth_register_elements\"])();\n    _this.onChange = _this.onChange.bind(_assertThisInitialized(_assertThisInitialized(_this)));\n    _this.onSubmit = _this.onSubmit.bind(_assertThisInitialized(_assertThisInitialized(_this)));\n    return _this;\n  }\n\n  _createClass(Register, [{\n    key: \"onChange\",\n    value: function onChange() {\n      var _this2 = this;\n\n      Object.values(this.elements).map(function (el) {\n        el.onchange = _this2.changeEventHandler;\n      });\n    }\n  }, {\n    key: \"changeEventHandler\",\n    value: function changeEventHandler(event) {\n      var change = _defineProperty({}, event.target.name, event.target.value);\n\n      console.log(change);\n      this.setState(change);\n    }\n  }, {\n    key: \"onSubmit\",\n    value: function onSubmit() {\n      var _this3 = this;\n\n      var errors = _objectSpread({}, this.state.errors);\n\n      var submit = this.elements.submit;\n      submit.addEventListener(\"click\", function (e) {\n        e.preventDefault();\n        var data = _this3.state;\n        console.log(data); // this.api.post(this.url, this.state);\n      });\n    }\n  }]);\n\n  return Register;\n}(_common_App__WEBPACK_IMPORTED_MODULE_0__[\"Component\"]);\n\n/* harmony default export */ __webpack_exports__[\"default\"] = (Register);\n\n//# sourceURL=webpack:///./UI/js/components/Register.js?");

/***/ }),

/***/ "./UI/js/index.js":
/*!************************!*\
  !*** ./UI/js/index.js ***!
  \************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _components_Register__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./components/Register */ \"./UI/js/components/Register.js\");\n // Initializing the classes\n\nvar register = new _components_Register__WEBPACK_IMPORTED_MODULE_0__[\"default\"](); // Register events\n\nregister.onChange();\nregister.onSubmit();\n\n//# sourceURL=webpack:///./UI/js/index.js?");

/***/ })

/******/ });