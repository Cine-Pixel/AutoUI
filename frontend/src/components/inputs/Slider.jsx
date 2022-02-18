import { Slider as Slide, InputLabel } from "@mui/material";
import PropTypes from "prop-types";

const Slider = ({ label, minimum, maximum, step }) => (
  <>
    <InputLabel>{label}</InputLabel>

    <Slide
      valueLabelDisplay="auto"
      defaultValue={0}
      step={step}
      min={minimum}
      max={maximum}
    />
  </>
);

Slider.propTypes = {
  label: PropTypes.string,
  minimum: PropTypes.number,
  maximum: PropTypes.number,
  step: PropTypes.number,
};

Slider.defaultProps = {
  label: "",
  minimum: 0,
  maximum: 10,
  step: 1,
};

export default Slider;
