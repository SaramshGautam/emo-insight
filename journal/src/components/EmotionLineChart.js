import React from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const EmotionLineChart = ({ data }) => {
  return (
    <div className="emotion-line-chart">
      <h3>Emotions Over Time</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart
          data={data}
          margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="happy" stroke="#4caf50" />
          <Line type="monotone" dataKey="sad" stroke="#f44336" />
          <Line type="monotone" dataKey="angry" stroke="#ff9800" />
          <Line type="monotone" dataKey="anxious" stroke="#2196f3" />
          <Line type="monotone" dataKey="confused" stroke="#9c27b0" />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default EmotionLineChart;
