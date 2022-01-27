import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import { withStyles } from '@material-ui/core';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import API from '../api/API';


class SpoStudyCoursesList extends Component {

    constructor(props) {
        super(props);

        this.state = {
			spoStudyCoursesList: [],
            loadingProgress: false,
            studyCourseId: null,
            error: null,
        };
    }

	componentDidMount() {
		const id = this.props.match.params.studyCourseID;
		API.getAPI().getAllSpoRelated(id).then((spos) => {
            if (spos && spos.length) {
                this.setState({
                    spoStudyCoursesList: spos,
                    loadingProgress: false,
                    error: null
                });
            } else {
                this.setState({
                    spoStudyCoursesList: [],
                    loadingProgress: false,
                    error: null
                });
            }			
		}).catch((error) => {
			this.setState({
				loadingProgress: false,
				error: error
			});
		});
		this.setState({
            loadingProgress: true,
            studyCourseId: id,
            error: null
        });
    }

    onButtonSpoClocked(id) {
        this.props.history.push(`/admin/${this.state.studyCourseId}/${id}`);
    }

    render() {
        const { classes } = this.props;
        const { loadingProgress, error, spoStudyCoursesList} = this.state;
        return (

            <Box sx={{ width: '100%', maxWidth: 650, marginLeft: 'auto', marginRight: 'auto'    }}>
     
                <Typography variant="h6" textAlign={'center'} gutterBottom component="div">
                    Wähle ein Semester
                </Typography>
                    
                <Stack spacing={2} direction="column">
                    {
                        spoStudyCoursesList.map((spo) => (
                        <Button
                            variant="contained"
                            key={spo.id}
                            onClick={this.onButtonSpoClocked.bind(this, spo.id)}
                            show ={this.props.show}>
                                {spo.name}
                        </Button>
                        ))
                    }
                </Stack>
            </Box>
        )
    }
}

/** Component specific styles */
const styles = theme => ({
    root: {
        width: '100%',
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(2),
    },
    content: {
        margin: theme.spacing(1),
    },
    table: {
        minWidth: 700,
    },
    header:{
        marginBottom: theme.spacing(1),
        paddingLeft: theme.spacing(1),
        paddingRight: theme.spacing(1),
    },
    button:{
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(3),
        float: 'right'
    }
});

/** PropTypes */
SpoStudyCoursesList.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
    /** @ignore */
    location: PropTypes.object.isRequired,
   
}


export default withRouter(withStyles(styles)(SpoStudyCoursesList));