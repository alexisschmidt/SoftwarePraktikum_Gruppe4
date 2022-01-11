import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Paper, Typography, Tabs, Tab } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';
import ProfileDropDown from '../dialogs/ProfileDropDown';


class Header extends Component {

  constructor(props) {
    super(props);

    // Initiieren eines leeren Zustands
    this.state = {
      tabindex: 0
    };
  }

  
  handleTabChange = (e, newIndex) => {
    this.setState({
      tabindex: newIndex
    })
  };

  render() {
    const { user } = this.props;

    return (
      <Paper variant='outlined' >
          <ProfileDropDown user={user} />
        <Typography variant='h3' component='h1' align='center'>
          Verwaltung der STUDIEN- UND PRÜFUNGSORDNUNGEN / SPO
        </Typography>
        {
          user ?
            <Tabs indicatorColor='primary' textColor='primary' centered value={this.state.tabindex} onChange={this.handleTabChange} >
              <Tab label='About' component={RouterLink} to={`/about`} />
              <Tab label='Admin' component={RouterLink} to={`/admin`} />

            </Tabs>
            : null
        }
      </Paper>
    )
  }
}

/** PropTypes */
Header.propTypes = {
  /** Angemeldeter Firebase Nutzer */
  user: PropTypes.object,
}

export default Header;