import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Model Persediaan EOQ (Economic Order Quantity)")

st.sidebar.header("Input Parameter")
D = st.sidebar.number_input("Permintaan Tahunan (unit)", min_value=1, value=12000)
S = st.sidebar.number_input("Biaya Pemesanan per Order (Rp)", min_value=1, value=150000)
H = st.sidebar.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=1, value=2500)

st.markdown("### Hasil Perhitungan EOQ")
EOQ = np.sqrt((2 * D * S) / H)
total_orders = D / EOQ

st.write(f"**EOQ (Jumlah Ekonomis Pemesanan):** {EOQ:.2f} unit")
st.write(f"**Jumlah Order per Tahun:** {total_orders:.2f} kali")

# Grafik Total Cost vs Order Quantity
st.markdown("### Visualisasi: Total Biaya vs Jumlah Pemesanan")
Q = np.arange(100, D + 500, 100)
ordering_cost = (D / Q) * S
holding_cost = (Q / 2) * H
total_cost = ordering_cost + holding_cost

fig, ax = plt.subplots()
ax.plot(Q, total_cost, label="Total Cost", color='blue')
ax.plot(Q, ordering_cost, label="Ordering Cost", linestyle='--', color='green')
ax.plot(Q, holding_cost, label="Holding Cost", linestyle='--', color='orange')
ax.axvline(EOQ, color='red', linestyle=':', label=f"EOQ ≈ {EOQ:.0f}")
ax.set_xlabel("Jumlah Pemesanan per Order (Q)")
ax.set_ylabel("Biaya (Rp)")
ax.set_title("Grafik Total Biaya Persediaan")
ax.legend()
st.pyplot(fig)

st.markdown("---")
st.markdown("📌 *Model EOQ membantu perusahaan menentukan jumlah pemesanan optimal agar biaya total minimum.*")
