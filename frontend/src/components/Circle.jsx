export default function Circle(props) {
  const { val, zoom } = props.data;
  const diameter = `${15 * val * Math.log(zoom)}px`

  const circleStyle = {
    width: diameter,
    height: diameter,
    borderRadius: '50%',
    backgroundColor: 'red',
    opacity: 0.75,
  };

  return (
    <div style={circleStyle}></div>
  );
}
