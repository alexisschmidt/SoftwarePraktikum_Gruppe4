import React, { Component } from 'react';
import PropTypes from 'prop-types'; /**ein Mechanismus, um sicherzustellen, dass Komponenten den richtigen Datentyp verwenden und die richtigen Daten übergeben*/
import { Button, Grid, Typography, withStyles } from '@material-ui/core';

class SignIn extends Component {
		
	handleSignInButtonClicked = () => {
		this.props.onSignIn();
	}

	/** Renders the sign in page, if user objext is null */
	render() {
		const { classes } = this.props;

		return (
			<div>
				<Typography className={classes.root} align='center' variant='h6'>Herzlich willkommen bei den SpO-Funktionen der HdM Stuttgart für Studierende, Lehrende und Mitarbeiter</Typography>
				<Typography className={classes.root} align='center'>Es scheint, dass Sie nicht angemeldet sind.</Typography>
				<Typography className={classes.root} align='center'>Um die SpO-Funktion nutzen zu können melden Sie sich bitte an!</Typography>
				<Grid container justify='center'>
					<Grid item>
						<Button variant='contained' color='primary' onClick={this.handleSignInButtonClicked}>
							Sign in with Google
      			</Button>
					</Grid>
				</Grid>
			</div>
		);
	}
}

/** Component specific styles */
const styles = theme => ({
	root: {
		margin: theme.spacing(2)
	}
});

/** PropTypes */
SignIn.propTypes = {
	/** @ignore */
	classes: PropTypes.object.isRequired,
	/**Handlerfunktion, die aufgerufen wird, wenn sich der Benutzer anmelden möchte.*/

	onSignIn: PropTypes.func.isRequired,
}

export default withStyles(styles)(SignIn)