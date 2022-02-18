import { TextField } from "@mui/material";
import PropTypes from "prop-types";

const Number = ({ label, placeholder }) => (
  <TextField fullWidth size="small" label={label} placeholder={placeholder} />
);

Number.propTypes = {
  label: PropTypes.string,
  placeholder: PropTypes.string,
};

Number.defaultProps = {
  label: "",
  placeholder: "",
};

export default Number;
