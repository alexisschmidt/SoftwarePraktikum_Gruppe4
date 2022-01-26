import React, { Component } from "react";
import PropTypes from "prop-types";
import API from "../api/API";
import ContextErrorMessage from "./dialogs/ContextErrorMessage";
import LoadingProgress from "./dialogs/LoadingProgress";
import {ListItem, TableCell, TableRow, Button } from "@material-ui/core";
import { Studycourses } from '../api/BusinessObjects';
//import StudyCourseDeleteDialog from "../components/dialogs/StudyCourseDeleteDialog";
import StudyCourseUpdateForm from "./dialogs/StudyCourseUpdateForm";
import DeleteIcon from '@material-ui/icons/Delete';

class AllStudycoursesEntry extends Component {

        constructor(props) {
            super(props);
        
            this.state = {
                studycourses: this.props.studycourses,
                loadingProgress: false,
                error: null,
                showStudyCourseDeleteDialog: false,
                showStudyCourseUpdateForm: false,
            }
        }

        getAllStudycourses = () => {
            this.props.getAllStudycourses();
        }

        studycoursesDeleteClosed = (studycourses) => {
            if (studycourses) {
                this.setState({
                    studycourses: studycourses,
                    showStudyCourseDeleteDialog: false
                });
            } else {
                this.setState({
                    showStudyCourseDeleteDialog: false
                });
            }
        }

        openDeleteStudyCourses = event =>  {
            event.stopPropagation();
            this.setState({showStudyCoursesDeleteDialog: true})
        }
        openEditModal = event => {
            event.stopPropagation();
    
            this.setState({
                showStudyCoursesUpdateForm: true
            })
        }

        studycoursesUpdateFormClosed = studycourses => {
            if (studycourses) {
                //const newStudiengang = [...this.state.studiengang, studiengang];
                this.setState({
                    studycourses: studycourses,
                    showStudyCoursesUpdateForm: false,
    
                });
            } else {
                this.setState({
                    showStudyCoursesUpdateForm: false,
    
                });
            }
        }






    

        render() {
            const { classes, studycourses } = this.props;
            const { loadingProgress, error, showStudyCoursesDeleteDialog, showStudyCoursesUpdateForm} = this.state;
          
            return (
                <TableRow key={studycourses}>
                <TableCell component="th" scope="row">
                    {studycourses.id}
                </TableCell>
                <TableCell component="th" scope="row">
                    {studycourses.semester}
                </TableCell>
                <TableCell component="th" scope="row">
                    {studycourses.abschluss}
                </TableCell>
                <TableCell component="th" scope="row">
                    {studycourses.engl_titel}
                </TableCell>
                <TableCell component="th" scope="row">
                    {studycourses.name}
                </TableCell>
                <TableCell component="th" scope="row">
                    {studycourses.creation_date}
                </TableCell>
                <TableCell>
                    <Button variant = "contained" color = 'primary' size = "small" onClick={this.oeffneEditModal}>
                            Edit
                        </Button>
                        <StudyCourseUpdateForm show = {showStudyCoursesUpdateForm} studycourses={studycourses} onClose = {this.studyCoursesUpdateFormClosed} />
                        </TableCell>
                        <TableCell>
                        <Button aria-label="delete"  variant="outlined">
                          <DeleteIcon fontSize="small" onClick={() => this.props.deleteStudyCoursesHandler(this.props.studycourses.getID())}/>
                        </Button>
                      
                </TableCell>

            </TableRow>
            )
        }

}
/** PropTypes */
AllStudycoursesEntry.propTypes = {
    /** @ignore */
  
    studycourses: PropTypes.object.isRequired,
}
export default AllStudycoursesEntry;