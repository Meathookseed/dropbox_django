import React from 'react';
import PropTypes from 'prop-types';
import { Button, Form, FormGroup, Label, Input, FormText } from 'reactstrap';
import '../App.css'
class LoginForm extends React.Component {
  state = {
    username: '',
    password: ''
  };

  handle_change = e => {
    const name = e.target.name;
    const value = e.target.value;
    this.setState(prevstate => {
      const newState = { ...prevstate };
      newState[name] = value;
      return newState;
    });
  };

  render() {
    return (
      <Form onSubmit={e => this.props.handle_login(e, this.state)}>
          <FormGroup>
        <h4>Log In</h4>
        <Label for="examplePassword">Username</Label>
        <input
          type="text"
          name="username"
          value={this.state.username}
          placeholder="type your password"
          onChange={this.handle_change}
        />
          </FormGroup>
          <FormGroup>
        <label htmlFor="password">Password</label>
        <Input
          type="password"
          name="password"
          value={this.state.password}
          onChange={this.handle_change}
        />
        <Input type="submit" />
          </FormGroup>
      </Form>
    );
  }
}

export default LoginForm;

LoginForm.propTypes = {
  handle_login: PropTypes.func.isRequired
};