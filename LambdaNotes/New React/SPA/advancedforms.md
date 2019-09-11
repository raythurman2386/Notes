# Advanced forms with the Formik Library

Formik is a helper library that is recognized as one of the best form-management utilities currently available.
Formik abstracts away some of the more complex situations we may come across
like:
Nested form data or arrays
Wiring up state
Validation
Error messages

    npm install formik --save

> Using the form from the last section and removed the state-handling hooks, handleChange and handleSubmit from the previous form

    import React from "react";
    import { withFormik, Form, Field } from "formik";

    function LoginForm() {
      //removed all of the previous code (state-management, change/submit-handlers)

      return (
        <div className="loginForm">
          {console.log(user)}
          <form onSubmit={event => handleSubmit(event)}>
            <label>
              Username:
              <input
                type="text"
                name="username"
                onChange={event => handleChange(event)}
              />
            </label>
            <label>
              Password:
              <input
                type="text"
                name="password"
                onChange={event => handleChange(event)}
              />
            </label>
            <button>Submit!</button>
          </form>
        </div>
      );
    }

    export default LoginForm;

The main form tag from formik will just need added which means capitalizing the main form tags and the onchange may be removed
also all inputs now become `Fields` and `labels` get changed to `placeholder`

    <Form>
      <Field
        type="text"
        name="username"
        placeholder="Username"
      />
      <Field
        type="text"
        name="password"
        placeholder="Password"
      />
      <button>Submit!</button>
    </Form>

From here the form will still not work.
We need to wire the form up with Formik

We take our LoginForm function and wrap it inside the Higher-order Formik component using `withFormik`

    const FormikLoginForm = withFormik({
      mapPropsToValues({ username, password }) {
        return {
          username: username || "",
          password: password || "",
        }
      }
    })(LoginForm);

`mapPropsToValues` allows us to create a connection between the data being handled in the form and the handlers for the data. The conditional values for the key-values allow you to pass in default or custom data to the form initially.

To handle submits with you will use the following

    const FormikLoginForm = withFormik({
      mapPropsToValues({ email, password }) {
        return {
          email: email || "",
          password: password || "",
        }
      },

      handleSubmit(values) {
        console.log(values)
        // This is where you do your form submission code
      }
    })(LoginForm);

## Learn to validate user forms

A very popular method for validating forms is a library named `Yup`
Formik author is such a fan of Yup that he integrated a lot of code handling for Yup support directly

    const FormikLoginForm = withFormik({
      mapPropsToValues({ email, password }) {
        return {
          email: email || "",
          password: password || "",
        }
      },

      //=========================

      validationSchema: Yup.object().shape({
        email: Yup.string()
          .email()
          .required(),
        passwork: Yup.string()
          .min(6)
          .required()
      })

      //=========================

      handleSubmit(values) {
        console.log(values)
        // This is where you do your form submission code
      }
    })(LoginForm);

And now to hook it up to our form for validation

    // Adding destructured 'errors' prop to the form. The 'errors' prop gets passed down from the 'withFormik' component.
    function LoginForm({ errors }) {
      return (
        <Form>
          <div>
            {touched.email && errors.email && <p>{errors.email}</p>} //if there is an error, this
            shows you the errors message.
            <Field type="email" name="email" placeholder="Email" />
          </div>
          <div>
          {touched.password && errors.password && <p>{errors.password}</p>}
            <Field type="password" name="password" placeholder="Password" />
          <button>Submit!</button>
        </Form>
      );
    }

Now lets add custom erros to our schema from above

    validationSchema: Yup.object().shape({
        email: Yup.string()
          .email("Email Not Valid")
          .required("Email is Required"),
        passwork: Yup.string()
          .min(6, "Password must be at least 6 characters")
          .required("Password Required")
      })

Now lets make a dropdown field and a checkbox field

    <Field component="select" name="meal">
      <option value="gold">Gold</option>
    </Field>

    <label>
      <Field type="checkbox" name="tos" checked={values.tos} />
      Accept TOS
    </label>

We wrap the checkbox with a label so we can make the checkbox text also clickable
Now we need to make sure we wire up those components to the `mapPropsToValues`

    import React from "react";
    import { withFormik, Form, Field } from "formik";
    import * as Yup from "yup";

    function LoginForm({ values, errors, touched }) {
      return (
        <Form>
          <div>
            {touched.email && errors.email && <p>{errors.email}</p>}
            <Field type="email" name="email" placeholder="Email" />
          </div>
          <div>
            {touched.password && errors.password && <p>{errors.password}</p>}
            <Field type="password" name="password" placeholder="Password" />
          </div>
          <Field component="select" name="meal">
            <option value="gold">Gold</option>
            <option value="silver">Silver</option>
            <option value="platinum">Platinum</option>
          </Field>
          <label>
            <Field type="checkbox" name="tos" checked={values.tos} />
            Accept TOS
          </label>
          <button>Submit!</button>
        </Form>
      );
    }

    const FormikLoginForm = withFormik({
      mapPropsToValues({ email, password, tos, meal }) {
        return {
          email: email || "",
          password: password || "",
          tos: tos || false,
          meal: meal || "silver"
        };
      },

      validationSchema: Yup.object().shape({
        email: Yup.string()
          .email("Email not valid")
          .required("Email is required"),
        password: Yup.string()
          .min(6, "Password must be 6 characters or longer")
          .required("Password is required")
      }),

      handleSubmit(values) {
        console.log(values);
        //THIS IS WHERE YOU DO YOUR FORM SUBMISSION CODE... HTTP REQUESTS, ETC.
      }
    })(LoginForm);

    export default FormikLoginForm;
