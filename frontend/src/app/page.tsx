export default function HomePage() {
  return (
    <main className="mx-auto max-w-5xl px-4 py-12">
      <header className="mb-8 border-b border-slate-200 pb-6">
        <h1 className="text-3xl font-bold tracking-tight text-slate-900">
          DevConnect
        </h1>
        <p className="mt-2 text-slate-600">
          Nền tảng chia sẻ kiến thức công nghệ và bài viết kỹ thuật.
        </p>
      </header>
      <section className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <h2 className="text-lg font-semibold text-slate-800">
          Khung dự án Frontend đã sẵn sàng
        </h2>
        <p className="mt-2 text-sm text-slate-600">
          Xem tài liệu thiết kế tại <code>docs/SYSTEM_DESIGN.md</code> và quy
          trình làm việc tại <code>docs/DEVELOPMENT_PROCESS.md</code>.
        </p>
      </section>
    </main>
  );
}
